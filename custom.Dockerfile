FROM unitycatalog/unitycatalog:v0.3.0

USER root
# RUN apk add --no-cache libc6-compat 
COPY server/target/classes /home/unitycatalog/server/target/classes
COPY server/target/unitycatalog-server-0.3.0.jar /home/unitycatalog/server/target/
COPY bin/start-uc-server /home/unitycatalog/bin/
COPY etc/jars/mysql-connector-j-8.0.31.jar /home/unitycatalog/etc/jars/
COPY etc/conf /home/unitycatalog/etc/conf
RUN  chmod +x /home/unitycatalog/bin/start-uc-server
RUN  chown -R unitycatalog:unitycatalog /home/unitycatalog

ENV JAVA_OPTS="-Xmx1512m -Xms512m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=256m"

COPY etc/oauth-selfsigned-simple.crt /tmp/
RUN keytool -importcert -noprompt \
    -alias mycert \
    -file /tmp/oauth-selfsigned-simple.crt \
    -keystore $JAVA_HOME/lib/security/cacerts \
    -storepass changeit

USER unitycatalog
