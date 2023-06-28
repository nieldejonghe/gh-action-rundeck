# rundeck-action
Github Action to execute Rundeck jobs

Example usage: 
```yaml
  deploy:
    needs: publish
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to ${{ env.DEPLOY_ENVIRONMENT }}
        env: 
            VERSION: ${{ needs.publish.outputs.VERSION }}
            IMAGE_TAG: ${{ needs.publish.outputs.IMAGE_TAG }}
        uses: <ghreponame>/gh-action-rundeck@main
        with: 
          rundeck-url: <rundeck endpoint>
          rundeck-token: <rundeck api token>
          job-id: <job id>
          verify-ssl: false
          rundeck-job-options: |
            {
              "app_version": "${{ env.VERSION }}-${{ env.IMAGE_TAG }}",
              "branch": "master",
              "environment": "${{ env.DEPLOY_ENVIRONMENT }}",
              "service": "${{ env.PRODUCT }}/${{ env.SERVICE }}"
            }
          wait: true

```
