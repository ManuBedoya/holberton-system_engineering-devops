# Increment the limits
exec{ 'fix limit':
      command => 'sed -i "$ d" /etc/default/nginx; echo ULIMIT=\"-n $(ulimit -n)\" >> /etc/default/nginx; sudo service nginx restart',
      path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',

}