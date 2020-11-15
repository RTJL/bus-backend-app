# Serverless Framework + AWS Backend
Basic steps needed to get API gateway with a custom domain name and serverless functions working using the serverless framework.

## Outline of Steps
1. Link domain to AWS Route 53
2. Create domain using Serverless framework
3. Create AWS resources using Serverless framework

---

### Link domain to AWS Route 53

1. Register a domain

    [freenom](https://freenom.com/) provides free `.tk` domains.

1. Get a AWS certificate for your domain registar
    1. Go to Certificate Manager
    2. Request a public certificate
    3. Enter your domain name
    4. Choose email or DNS confirmation
    - If email, click approve upon receiving email
    - If DNS, go to domain registar and update the CNAME

2. Transfer DNS control from domain registar to AWS
    1. Go to Route53
    2. Create a new hosted zone
    3. Enter domain name
    4. Go back to domain registar and update nameserver(NS) values

### Create domain using Serverless framework

1. Install **serverless-domain-manager** plugin

    `npm install serverless-domain-manager`

2. Add the plugin configuration to `serverless.yml` config file

3. Create domain using the serverless command 

    `sls create_domain --stage dev`

### Create AWS resources using Serverless framework

1. Add the provider and functions to `serverless.yml` config file

2. Create AWS resources using the serverless command

    `sls deploy --stage dev`