{{- define "sre-app.labels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{- define "sre-app.selectorLabels" -}}
app: {{ .Values.app.name }}
{{- end -}}