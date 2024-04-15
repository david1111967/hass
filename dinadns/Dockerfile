ARG BUILD_FROM
FROM $BUILD_FROM

# Setup base
ARG DEHYDRATED_VERSION
RUN apk add --no-cache openssl \
  && curl -s -o /usr/bin/dehydrated \
    "https://raw.githubusercontent.com/lukas2511/dehydrated/v${DEHYDRATED_VERSION}/dehydrated" \
  && chmod a+x /usr/bin/dehydrated

# Copy data
COPY data/*.sh /

RUN mkdir -p /var/www/dehydrated
RUN chmod 755 /var/www/dehydrated

RUN chmod a+x /run.sh
RUN chmod a+x /hooks.sh
RUN chmod a+x /usr/bin/dehydrated

CMD [ "/run.sh" ]
