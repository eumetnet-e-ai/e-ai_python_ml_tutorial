FROM python:3.10-slim-bookworm
ARG DEBIAN_FRONTEND=noninteractive

USER root
# Run basesetup
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash dwd
USER dwd

WORKDIR /home/dwd

COPY --chown=dwd face.py .
COPY --chown=dwd requirements.txt .

# Set environment variables for the virtual environment
ENV VIRTUAL_ENV=/home/dwd/venv
# Make virtual environment accessible
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN cd /home/dwd && python3 -m venv $VIRTUAL_ENV

RUN pip3 install -r requirements.txt

CMD python3 face.py
