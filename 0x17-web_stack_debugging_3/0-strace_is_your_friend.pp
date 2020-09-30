# Fix typo in wordpress settings
exec { 'replace':
path    => '/bin',
command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
