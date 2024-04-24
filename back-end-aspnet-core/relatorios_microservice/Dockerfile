# Dockerfile do relatorios_microservice

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY . .
RUN dotnet restore "relatorios_microservice.csproj"
RUN dotnet build "relatorios_microservice.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "relatorios_microservice.csproj" -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/core/aspnet:3.1 AS runtime
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "relatorios_microservice.dll"]
