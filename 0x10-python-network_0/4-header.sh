#!/bin/bash
# curl sends GET req to URL, displays response body
# display a custom header
curl -sH "X-School-User-Id: 98" "$1"
