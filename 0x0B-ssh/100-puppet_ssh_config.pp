# client ssh configuration
# Without password
file_line{'idintety_file':
  path => '~/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}

file_line{'idintety_file_psw':
  path => '~/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
