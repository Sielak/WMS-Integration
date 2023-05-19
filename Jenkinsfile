def getEnvFromBranch(branch) {
  if (branch == 'master') {
    return 'BMA-WMS-101'
  } else if (branch == 'test') {
    return 'BMA-APP-701'
  } else {
    return 'BMA-DEV-704'
 }
}
def choosed_agent = getEnvFromBranch(env.BRANCH_NAME)

pipeline {
    agent {
        label "${choosed_agent}"
    }
	options {
      gitLabConnection('gitlab')
      gitlabBuilds(builds: ['Build', 'Test', 'Deploy'])
    }
    stages {
        stage('Build') {
            steps {
                // Get some code from a GitLab repository
                updateGitlabCommitStatus name: 'Build', state: 'pending'
				sh '''
                    . /home/ubuntu/virtual_environments/venv_wms2.0/bin/activate
                    pip install -r requirements.txt
                '''
                updateGitlabCommitStatus name: 'Build', state: 'success'
            }
        }
		stage('Test') {
            steps {
                updateGitlabCommitStatus name: 'Test', state: 'pending'
                sh '''
                    . /home/ubuntu/virtual_environments/venv_wms2.0/bin/activate
                    coverage run --source=. -m pytest
                    coverage json --pretty-print
                '''
            }
			post {
				failure {
					echo "[INFO] Unit Tests failed"
                    archiveArtifacts artifacts: 'coverage.json'
                    updateGitlabCommitStatus name: 'Test', state: 'failed'
				}
                success {
					archiveArtifacts artifacts: 'coverage.json'
                    updateGitlabCommitStatus name: 'Test', state: 'success'
				}
			}
        }
		stage('Deploy') {
            when { 
                anyOf { 
                    branch 'master'; 
                    branch 'test' 
                } 
            }
            steps {
                updateGitlabCommitStatus name: 'Deploy', state: 'pending'
                sh 'sudo systemctl stop wms2.0.service'
                sh 'sudo rm -rf /opt/wms2.0/'
                sh 'sudo mkdir /opt/wms2.0'
				sh 'sudo mv * /opt/wms2.0'
                sh 'sudo cp /home/ubuntu/.config/wms2.0/config.json /opt/wms2.0/config/config.json'
                sh 'sudo systemctl start wms2.0.service'
                echo 'New version installed'
                updateGitlabCommitStatus name: 'Deploy', state: 'success'
            }
        }
        stage('Deploy - dev') {
            when { 
                not { 
                    anyOf { 
                        branch 'master'; 
                        branch 'test' 
                    } 
                } 
            }
            steps {
                updateGitlabCommitStatus name: 'Deploy', state: 'pending'
                echo 'Inform GitLab pipeline about status of dev build'
                updateGitlabCommitStatus name: 'Deploy', state: 'success'
            }
        }
    }
	post {
        always {
            cleanWs deleteDirs: true, notFailBuild: true
        }
		failure{			
			emailext body: "Job Failed<br>URL: ${env.BUILD_URL}", 
                    recipientProviders: [[$class: 'DevelopersRecipientProvider']],
					subject: "Job: ${env.JOB_NAME}, Build: #${env.BUILD_NUMBER} - Failure !",
					attachLog: true
        }
        success{			
			emailext body: "Job builded<br>URL: ${env.BUILD_URL}", 
                    recipientProviders: [[$class: 'DevelopersRecipientProvider']],
					subject: "Job: ${env.JOB_NAME}, Build: #${env.BUILD_NUMBER} - Success !",
					attachLog: true
        }
    }
}
