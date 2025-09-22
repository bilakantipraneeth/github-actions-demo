FROM alpine:latest

WORKDIR /app

RUN apk update && \
    apk add --no-cache bash coreutils

COPY show_directory.sh .

RUN chmod +x show_directory.sh

CMD ["./show_directory.sh"]