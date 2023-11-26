# Manifest to make changes to Confirguration file

file { 'configured':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}

file { 'No password authentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
