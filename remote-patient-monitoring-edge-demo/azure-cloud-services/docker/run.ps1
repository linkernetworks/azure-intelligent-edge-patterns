docker run -v ${pwd}:/work -v $HOME\.azure\:/root/.azure/ --workdir='/work' mcr.microsoft.com/azure-cli /work/docker/deploy.sh
