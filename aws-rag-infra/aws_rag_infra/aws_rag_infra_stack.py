from aws_cdk import (
    Stack,
    Duration,
    CfnOutput,
    aws_lambda as lambda_,
    aws_iam as iam
)
from constructs import Construct

class AwsRagInfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

       # Function to handle the API requests
        api_image_code = lambda_.DockerImageCode.from_image_asset(
            "../rag_pipeline",
            cmd=["src/app_api_handler.handler"],
            build_args={
                "platform": "linux/amd64"
            }
        )
        
        api_function = lambda_.DockerImageFunction(
            self, "ApiFunc",
            code=api_image_code,
            memory_size=256,
            timeout=Duration.seconds(300),
            architecture=lambda_.Architecture.X86_64
        )

        # Public URL for the API function
        function_url = api_function.add_function_url(
            auth_type=lambda_.FunctionUrlAuthType.NONE
        )

        # Grant permissions
        api_function.role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonBedrockFullAccess")
        )

        # Output the URL for the API function
        CfnOutput(
            self, "FunctionUrl",
            value=function_url.url
        )
