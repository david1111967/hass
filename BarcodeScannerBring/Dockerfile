ARG BUILD_FROM
FROM $BUILD_FROM

# Copy data
COPY data/* /

RUN pip install -r /requirement.txt
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]