# install puppet-lint -v 2.5.0

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

exec { 'Verify Flask Version':
  command => 'flask --version',
  path    => ['/usr/local/bin', '/usr/bin', '/bin'],
  logoutput => true,
}
