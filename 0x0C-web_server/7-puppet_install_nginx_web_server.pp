# Using Puppet| Install Nginx server, setup and configuration

package { 'nginx':
  ensure => 'installed'
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'redirection-301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=7VAI73roXaY&t=2554s permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
