# Minimal Ruby image for building/serving the Jekyll (just-the-docs) site.
# The codelab markdown is already committed, so no codelab build step is
# needed here — this container is for previewing the site.
FROM docker.io/library/ruby:3.1

WORKDIR /usr/src/app

# Build toolchain needed by native gems (nokogiri, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Install the Ruby/Jekyll dependencies first (cached layer).
COPY Gemfile Gemfile.lock ./
RUN gem install bundler -v 2.5.10 && bundle install

# Copy the site.
COPY . .

# Port for `jekyll serve`.
EXPOSE 4000
