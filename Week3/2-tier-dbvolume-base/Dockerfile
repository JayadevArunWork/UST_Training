FROM eclipse-temurin:17-jdk-jammy

WORKDIR /app

COPY target/k8s-spring-demo-1.0.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java","-jar","app.jar"]
