FROM golang:1.23.0 as builder
LABEL authors="MeoBeu"

RUN adduser -u 1000 ctfer --disabled-password

WORKDIR /app

COPY app/go.mod app/go.sum ./
RUN go mod download

COPY app/ ./

RUN CGO_ENABLED=0 go build -a -ldflags '-w' -o app .

FROM alpine:3.18

COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group

COPY --from=builder --chown=ctfer:ctfer /app/app /app/app
COPY --chown=ctfer:ctfer app/assets /app/assets
COPY --chown=ctfer:ctfer app/statics /app/statics
COPY --chown=ctfer:ctfer app/templates /app/templates
COPY --chown=ctfer:ctfer app/robots.txt /app/robots.txt
COPY --chown=ctfer:ctfer app/passwords.txt /app/passwords.txt

COPY --chown=root entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /app
USER ctfer

EXPOSE 62233

ENTRYPOINT ["/entrypoint.sh"]