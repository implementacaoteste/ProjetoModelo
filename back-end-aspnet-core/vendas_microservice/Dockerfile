# Dockerfile do vendas_microservice

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY . .
RUN dotnet restore "vendas_microservice.csproj"
RUN dotnet build "vendas_microservice.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "vendas_microservice.csproj" -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/core/aspnet:3.1 AS runtime
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "vendas_microservice.dll"]
