# Install nginx and setup files

exec { 'exec_0':
	command => 'apt-get update -y',
  	path    => ['/usr/bin', '/bin'],
	returns => [0,1]
}

file_line { 'add-line':
    ensure   => 'present',
    after    => 'location / {',
    multiple => true,
    path     => '/etc/nginx/sites-available/default',
    line     => '\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n',
}

package { 'nginx':
	require => File_line['add-line'],
	ensure => installed,
	provider => 'apt',
	name => 'nginx'
}

exec { 'exec_1':
	command => 'mkdir -p /data/web_static/releases/test',
  	path    => ['/usr/bin', '/bin'],
	returns => [0,1]
}

exec { 'exec_2':
    require => Exec['exec_1'],
	command => 'mkdir /data/web_static/shared/',
  	path    => ['/usr/bin', '/bin'],
	returns => [0,1]
}

file { 'index.html':
  ensure  => file,
  path    => '/data/web_static/releases/test/',
  mode    => '0744',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>'
}

exec { 'exec_3':
    require => Exec['exec_2'],
	command => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
  	path    => ['/usr/bin', '/bin'],
	returns => [0,1]
}

exec { 'exec_4':
    require => Exec['exec_3'],
	command => 'chown -R ubuntu:ubuntu /data/',
  	path    => ['/usr/bin', '/bin'],
	returns => [0,1]
}



exec { 'exec_5':
    require => Exec['exec_4'],
	command => 'service nginx restart',
  	path    => ['/usr/bin', '/bin'],
	returns => [0,1]
}