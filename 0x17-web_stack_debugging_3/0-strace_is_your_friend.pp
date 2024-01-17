# Puppet script that replace a line from server files
# replaces the line "class-wp-locale.phpp" to "class-wp-locale.php" i.e the right extension


$file_to_edit = '/var/www/html/wp-settings.php'

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
