#!/bin/bash
set -e

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="/backups/backup_${TIMESTAMP}.sql"

echo "[$(date)] Iniciando backup do banco de dados..."

mysqldump -h $DB_HOST -u $DB_USER -p$DB_PASSWORD $DB_NAME > $BACKUP_FILE

echo "[$(date)] Backup salvo em: $BACKUP_FILE"

# Remove backups com mais de N dias
find /backups -name "*.sql" -mtime +${RETENTION_DAYS:-7} -delete
echo "[$(date)] Backups antigos removidos (retenção: ${RETENTION_DAYS:-7} dias)"

echo "[$(date)] Backup concluído com sucesso!"