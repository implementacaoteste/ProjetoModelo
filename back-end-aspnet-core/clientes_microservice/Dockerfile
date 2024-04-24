# Dockerfile do clientes_microservice

# FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build-env
# FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build

WORKDIR /src
COPY . .
RUN dotnet restore "clientes_microservice.csproj"
# RUN dotnet build "clientes_microservice.csproj" -c Release -o /app/build

# FROM build AS publish
# RUN dotnet publish "clientes_microservice.csproj" -c Release -o /app/publish

# FROM mcr.microsoft.com/dotnet/core/aspnet:3.1 AS runtime
# WORKDIR /app
# COPY --from=publish /app/publish .
# ENTRYPOINT ["dotnet", "clientes_microservice.dll"]

