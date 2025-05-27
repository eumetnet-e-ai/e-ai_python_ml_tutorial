
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

# Set environment variables for the virtual environment
ENV VIRTUAL_ENV=/home/dwd/venv
# Make virtual environment accessible
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN cd /home/dwd && python3 -m venv $VIRTUAL_ENV

COPY --chown=dwd requirements.txt .
RUN pip3 install -r requirements.txt

# Add face.py, make it executable and add it to PATH.
COPY --chown=dwd face.py .
RUN chmod 775 face.py && ln -s $PWD/face.py $VIRTUAL_ENV/bin/face.py

CMD face.py
