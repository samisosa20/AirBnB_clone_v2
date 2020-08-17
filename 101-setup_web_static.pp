# Install nginx and setup files

exec { 'exec_0':
	command => 'apt-get update -y',
  	path    => ['/usr/bin', '/bin'],
	returns => [0,1]
}

package { 'nginx':
	require => Exec['exec_0'],
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
  path    => '/data/web_static/releases/test/index.html',
  mode    => '0744',
  owner   => 'root',
  group   => 'root',
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
	command => "sed -i '29a \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default",
  	path    => ['/usr/bin', '/bin'],
	returns => [0,1]
}

exec { 'exec_6':
    require => Exec['exec_5'],
	command => 'service nginx restart',
  	path    => ['/usr/bin', '/bin'],
	returns => [0,1]
}
