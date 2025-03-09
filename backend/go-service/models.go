package main

type Log struct {
	ID          int    `json:"id"`
	IP          string `json:"ip"`
	UserAgent   string `json:"user_agent"`
	RequestPath string `json:"request_path"`
	Timestamp   string `json:"timestamp"`
}
