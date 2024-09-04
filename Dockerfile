FROM maven:3.8.5-openjdk-17 AS build

WORKDIR /app

COPY pom.xml .

RUN mvn dependency:go-offline

COPY src ./src

RUN mvn package -DskipTests


FROM eclipse-temurin:17-jre-alpine

WORKDIR /app

COPY --from=build /app/target/*.jar /app/my-calculator-app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "my-calculator-app.jar"]