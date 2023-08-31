# Forking https://github.com/christophetd/log4shell-vulnerable-app
FROM gradle:7.3.1-jdk17 AS builder
COPY --chown=gradle:gradle log4j/ /home/gradle/src
WORKDIR /home/gradle/src
RUN gradle bootJar --no-daemon


FROM openjdk:8u181-jdk-alpine
RUN mkdir /app
COPY --from=builder /home/gradle/src/build/libs/*.jar /app/spring-boot-application.jar
CMD ["java", "-jar", "/app/spring-boot-application.jar"]
