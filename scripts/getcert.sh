#!/usr/bin/env bash

# prints the PEM certificate of the given site
openssl s_client -connect $1 2>/dev/null </dev/null |  sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > trusted.pem