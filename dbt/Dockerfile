##
#  Generic dockerfile for dbt image building.
#  See README for operational details
##

# Top level build args --> mac1では不要
#ARG build_for=linux/amd64

##
# base image (abstract)
##
#FROM --platform=$build_for python:3.11.2-slim-bullseye as base

FROM python:3.11-bullseye as base

# N.B. The refs updated automagically every release via bumpversion
# N.B. dbt-postgres is currently found in the core codebase so a value of dbt-core@<some_version> is correct

ARG dbt_core_ref=dbt-core@v1.5.0
ARG dbt_postgres_ref=dbt-core@v1.5.0
#ARG dbt_redshift_ref=dbt-redshift@v1.6.0a1
#ARG dbt_bigquery_ref=dbt-bigquery@v1.6.0a1
ARG dbt_snowflake_ref=dbt-snowflake@v1.5.0
# ARG dbt_spark_ref=dbt-spark@v1.5.0

# special case args
ARG dbt_spark_version=all
ARG dbt_third_party

# System setup
RUN apt-get update \
  && apt-get dist-upgrade -y \
  && apt-get install -y --no-install-recommends \
    git \
    ssh-client \
    software-properties-common \
    make \
    build-essential \
    ca-certificates \
    libpq-dev \
    vim \
  && apt-get clean \
  && rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/*

# Env vars
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8


# Update python
RUN python -m pip install --upgrade pip setuptools wheel --no-cache-dir

# Set docker basics /root/.dbtに置くことを求められるため。
WORKDIR /root/
VOLUME /usr/app

# https://qiita.com/ieiringoo/items/04f73e5557b534dc694d
ENTRYPOINT []

##
# dbt-core
##
FROM base as dbt-core
RUN python -m pip install --no-cache-dir "git+https://github.com/dbt-labs/${dbt_core_ref}#egg=dbt-core&subdirectory=core"

##
# dbt-postgres
##
FROM base as dbt-postgres
RUN python -m pip install --no-cache-dir "git+https://github.com/dbt-labs/${dbt_postgres_ref}#egg=dbt-postgres&subdirectory=plugins/postgres"

##
# dbt-redshift
##
#FROM base as dbt-redshift
#RUN python -m pip install --no-cache-dir "git+https://github.com/dbt-labs/${dbt_redshift_ref}#egg=dbt-redshift"


##
# dbt-bigquery
##
#FROM base as dbt-bigquery
#RUN python -m pip install --no-cache-dir "git+https://github.com/dbt-labs/${dbt_bigquery_ref}#egg=dbt-bigquery"


##
# dbt-snowflake
##
#FROM base as dbt-snowflake
#RUN python -m pip install --no-cache-dir "git+https://github.com/dbt-labs/${dbt_snowflake_ref}#egg=dbt-snowflake"

# 一時的な場所にprofiles.ymlを格納しておく。
RUN mkdir -p /tmp/dbt
ADD profiles.yml /tmp/dbt/profiles.yml 

# dbt taskをおそらく作成するたびに作らないと。。。(うまい方法ないものか)
COPY orange /usr/app/orange
WORKDIR /usr/app/orange