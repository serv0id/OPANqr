PAN Card QR Code Reader python implementation based on com.pv.scr.pancardreader. Can be used to decode and verify (optional) QR codes found on PAN and e-PAN cards.

# Purpose
 There is no public specification for the "Enhanced 2.0 Secure QR Codes" and the android app is somewhat obfuscated to prevent reverse engineering. The repository tries to emulate the application through a python port of the logic and also makes for a good reverse engineering exercise.

 # Usage
 * Clone the repository.
 * `pip install -r requirements.txt`
 * Scan the QR code and pass the string either directly through `--string` or through a file using `--file`
 * Optionally, use the `--verify` flag to verify the signature contained in the QR code using the appropriate public key.
 * The results get saved to the `output` directory. 
 
# ToDo
* ~~Implement Signature Verification~~
* Properly parse PII element
* Tidy Code
* Implement business PAN parsing
