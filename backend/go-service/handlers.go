package main

import (
	"encoding/json"
	"log"
	"net/http"
)

type LogEntry struct {
	IP          string `json:"ip"`
	UserAgent   string `json:"user_agent"`
	RequestPath string `json:"request_path"`
}

func logRequest(w http.ResponseWriter, r *http.Request) {
	entry := LogEntry{
		IP:          r.RemoteAddr,
		UserAgent:   r.UserAgent(),
		RequestPath: r.URL.Path,
	}

	log.Printf("Received request: %+v", entry)

	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(map[string]string{"message": "Logged"})
}
