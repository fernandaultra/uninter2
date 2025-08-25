#!/bin/bash

# Script para testar os endpoints da API

BASE_URL="http://localhost:5000"

echo "🧪 Testando endpoints da API..."
echo "================================"

# Teste 1: Health check
echo "1. Testando health check..."
curl -s "$BASE_URL/health" | jq .
echo ""

# Teste 2: Rota principal
echo "2. Testando rota principal..."
curl -s "$BASE_URL/" | jq .
echo ""

# Teste 3: Coletar cursos do Google Ateliê Digital
echo "3. Testando coleta do Google Ateliê Digital..."
curl -s -X POST "$BASE_URL/api/coletar/google-atelie" | jq .
echo ""

# Teste 4: Coletar cursos do SENAI
echo "4. Testando coleta do SENAI..."
curl -s -X POST "$BASE_URL/api/coletar/senai" | jq .
echo ""

# Teste 5: Coletar cursos do Gov.br
echo "5. Testando coleta do Gov.br..."
curl -s -X POST "$BASE_URL/api/coletar/gov-br" | jq .
echo ""

# Teste 6: Coletar cursos do CIEE
echo "6. Testando coleta do CIEE..."
curl -s -X POST "$BASE_URL/api/coletar/ciee" | jq .
echo ""

echo "✅ Testes concluídos!"
