# Stage 1: Base Image for Building Dependencies
FROM php:8.2-fpm as build

# Install required dependencies
RUN apt-get update && apt-get install -y \
    git \
    zip \
    unzip \
    libpq-dev \
    libonig-dev \
    libzip-dev \
    && docker-php-ext-install pdo pdo_mysql pdo_pgsql mbstring zip

# Install Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Set working directory
WORKDIR /var/www

# Copy application files
COPY . .

# Install dependencies using Composer
RUN composer install --no-dev --optimize-autoloader

---

# Stage 2: Production Environment
FROM php:8.2-fpm

# Copy PHP extensions from build stage
COPY --from=build /usr/local/lib/php/extensions/ /usr/local/lib/php/extensions/
COPY --from=build /usr/local/etc/php/ /usr/local/etc/php/

# Set working directory
WORKDIR /var/www

# Copy the optimized application from the build stage
COPY --from=build /var/www /var/www

# Set proper permissions
RUN chown -R www-data:www-data /var/www

# Expose default PHP-FPM port
EXPOSE 9000

# Run PHP-FPM
CMD ["php-fpm"]