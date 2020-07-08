### Getting started

Make sure that you have the Openshift Pipelines operator installed. The operator can be installed from the operator hub using the instructions [here](https://github.com/openshift/pipelines-tutorial/blob/master/install-operator.md). 

#### Install the task

`oc create -f https://raw.githubusercontent.com/hanvitha/InflightAssistance/master/workflows-s2i.yaml`


#### Run the task

`oc create -f https://raw.githubusercontent.com/hanvitha/InflightAssistance/master/run.yaml`


This will start the task running. You can check the logs using `tkn pipeline logs -f` 