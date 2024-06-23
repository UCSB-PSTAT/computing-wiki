# Use an official Ruby runtime as a parent image
FROM docker.io/library/ruby:3.1

# Set the working directory in the container
WORKDIR /usr/src/app

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    nodejs \
    && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* /tmp/library-scripts

# Copy the Gemfile and Gemfile.lock into the image
COPY Gemfile ./

# Install Bundler and Jekyll dependencies
RUN gem install bundler && bundle install

# Copy the rest of the application code
COPY . .

# Install claat
RUN ./wiki.sh

# Expose port 4000 to view the site
EXPOSE 4000

# Expose port 35729 for livereload
EXPOSE 35729
