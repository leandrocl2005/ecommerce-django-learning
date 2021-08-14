from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
  def __init__(self):
    self.client_id = ""
    self.client_secret = ""
    if not self.client_id or not self.client_secret:
      raise ValueError("Please, set client_id and secret_id")
    self.environment = SandboxEnvironment(client_id=self.client_id,
                                          client_secret=self.client_secret)
    self.client = PayPalHttpClient(self.environment)
