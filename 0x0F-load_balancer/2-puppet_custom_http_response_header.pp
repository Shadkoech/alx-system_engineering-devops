# installation and configuration of the nginx server using puppet lint

package { 'nginx':
  ensure => installed,
}

#confirguring redirect
file_line { 'redirection':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://github.com/Shadkoech permanent;',
}

#Add custom HTTP header
file_line { 'X-Served-By':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'rewrite ^/redirect_me https://github.com/Shadkoech permanent;',
  line   => 'add_header X-Served-By ${::environment["HOSTNAME"]};',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
