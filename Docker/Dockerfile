FROM alpine:3.21.0

# Install required packages
RUN apk add --no-cache \
    bash \
    curl

# Copy the script
COPY ../cli/tempmail /usr/local/bin/
RUN chmod +x /usr/local/bin/tempmail

# Set bash as the default shell
SHELL ["/bin/bash", "-c"]

ENTRYPOINT ["tempmail"]
CMD ["help"]
