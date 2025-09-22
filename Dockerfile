FROM openjdk:21-jdk-slim
ARG JAR_FILE=github-actions-spring-boot/target/github-actions-spring-boot-0.0.1-SNAPSHOT.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]