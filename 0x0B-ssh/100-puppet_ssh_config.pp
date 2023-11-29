# Manifest to make changes to Confirguration file

file_line { 'configured':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}

file_line { 'No password authentication':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
}
