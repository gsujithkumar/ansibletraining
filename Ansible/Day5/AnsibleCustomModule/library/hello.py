#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

def sayHello(message):
    return message;

def main():
    module = AnsibleModule(
                argument_spec = dict(
                        greeting_msg=dict(type='str', required= True)
                )
            )
    msg = module.params['greeting_msg'];

    response = sayHello(msg);

    result = dict(
        message = response
    )

    module.exit_json(**result);

main();
