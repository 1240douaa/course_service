#!/bin/bash

# Script pour démarrer les microservices en développement

echo "🚀 Démarrage des microservices..."

# Couleurs pour les logs
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Fonction pour vérifier si un port est disponible
check_port() {
    if lsof -Pi :$1 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
        echo -e "${RED}❌ Port $1 est déjà utilisé${NC}"
        return 1
    else
        echo -e "${GREEN}✅ Port $1 est disponible${NC}"
        return 0
    fi
}

# Vérifier les ports
echo "📡 Vérification des ports..."
check_port 8000 || exit 1
check_port 8081 || exit 1

# Démarrer Student Service
echo -e "\n${BLUE}📚 Démarrage Student Service (port 8081)...${NC}"
cd student_service 2>/dev/null || echo "⚠️  Dossier student_service introuvable"
if [ -d "student_service" ]; then
    cd student_service
    python manage.py runserver 8081 &
    STUDENT_PID=$!
    echo "Student Service PID: $STUDENT_PID"
fi

# Attendre un peu
sleep 2

# Démarrer Course Service
echo -e "\n${BLUE}🎓 Démarrage Course Service (port 8000)...${NC}"
cd ../course_service 2>/dev/null || cd course_service
python manage.py runserver 8000 &
COURSE_PID=$!
echo "Course Service PID: $COURSE_PID"

echo -e "\n${GREEN}✅ Services démarrés !${NC}"
echo -e "
📋 URLs disponibles:
   - Course Service:  http://localhost:8000
   - Student Service: http://localhost:8081
   - Course API:      http://localhost:8000/api/courses/
   - Student API:     http://localhost:8081/api/students/
   - Course GraphQL:  http://localhost:8000/graphql/

💡 Pour arrêter les services: Ctrl+C ou kill $COURSE_PID $STUDENT_PID
"

# Attendre que l'utilisateur arrête les services
wait