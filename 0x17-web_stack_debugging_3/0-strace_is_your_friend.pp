# Writes a new file index.html to be served on curl

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => '<html><head><title>Welcome to My Website</title></head><body><h1>Hello, World!</h1></body></html>',
  mode    => '0644',
}
