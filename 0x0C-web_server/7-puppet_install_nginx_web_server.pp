# puppet manifest code automate works

package { 'nginx': 
  ensure => installed,
}

file_line { 'install':
  ensure => 'present',
  path  => '/etc/nginx/sites-enabled/default',
  after => 'listen 80  default_server;',
  line  => 'rewrite ^/redirect_me https://github.com/mgemoraw permanent;',
}

# creating index file
file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

# creating error page file
file {'/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

# restart service
exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}

# start service nginx
service { 'nginx':
  ensure => running,
  require => Package['nginx'],
}
