# pp to configure all
exec { 'update':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell'
}
->

package { 'nginx':
  ensure   => present,
  name     => 'nginx',
  provider => 'apt'
}
->

file { 'index':
  ensure  => present,
  path    => '/var/www/html/index.nginx-debian.html',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => 'Holberton School'
}
->

file { 'page_not_found':
  ensure  => present,
  path    => '/var/www/html/404.html',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => "Ceci n'est pas une page"
}
->

exec { 'redirect_me':
  command  => 'sed -i "48i \\\n\tlocation /redirect_me {\n\t\treturn 301 https://youtube.com;\n\t}" /etc/nginx/sites-available/default',
  user     => 'root',
  provider => 'shell'
}
->

exec { 'set 404':
  command  => 'sed -i "42i \\\n\terror_page 404 /404.html;" /etc/nginx/sites-available/default',
  user     => 'root',
  provider => 'shell'
}
->

exec { 'Set X-Served-By':
  command  => 'sed -i "48i \\\t\tadd_header X-Served-By $HOSTNAME always;" /etc/nginx/sites-available/default',
  user     => 'root',
  provider => 'shell'
}
->

exec { 'restart nginx':
  command  => 'service nginx restart',
  user     => 'root',
  provider => 'shell'
}