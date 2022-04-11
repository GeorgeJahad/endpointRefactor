import pprint
pp = pprint.PrettyPrinter(indent=4)

# works with https://github.com/apache/ozone/blob/e188058d2dff04fe56592313bbdc4e50bab7adcc/hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/NSSummaryEndpoint.java

# descriptors of text to be replaced
# format of each line in an entry is:
#      hyphens
#      input filename(currently unused),
#      first line of old file text to be overwritten
#      last line of old file text to be overwritten
#      blank line
#      copy file
#      first line of text to be inserted from copy file
#      last line line of text to be inserted copy file

data = '''----------
NSSummaryEndpoint.java
      namespaceSummaryResponse = new NamespaceSummaryResponse(EntityType.ROOT);
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/RootEntityHandler.java
  public NamespaceSummaryResponse getSummaryResponse()
  }
-------------------
NSSummaryEndpoint.java
      namespaceSummaryResponse =
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/VolumeEntityHandler.java
  public NamespaceSummaryResponse getSummaryResponse()
  }
-------------------
NSSummaryEndpoint.java
      namespaceSummaryResponse =
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/BucketEntityHandler.java
  public NamespaceSummaryResponse getSummaryResponse()
  }
-------------------
NSSummaryEndpoint.java
      long dirObjectId = getDirObjectId(names);
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/DirectoryEntityHandler.java
  public NamespaceSummaryResponse getSummaryResponse()
  }
-------------------
NSSummaryEndpoint.java
      namespaceSummaryResponse = new NamespaceSummaryResponse(EntityType.KEY);
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/KeyEntityHandler.java
  public NamespaceSummaryResponse getSummaryResponse()
  }
-------------------
NSSummaryEndpoint.java
      namespaceSummaryResponse =
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/UnknownEntityHandler.java
  public NamespaceSummaryResponse getSummaryResponse()
  }
-------------------
NSSummaryEndpoint.java
      List<OmVolumeArgs> volumes = listVolumes();
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/RootEntityHandler.java
  public DUResponse getDuResponse(
  }
-------------------
NSSummaryEndpoint.java
      String volName = names[0];
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/VolumeEntityHandler.java
  public DUResponse getDuResponse(
  }
-------------------
NSSummaryEndpoint.java
      long bucketObjectId = getBucketObjectId(names);
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/BucketEntityHandler.java
  public DUResponse getDuResponse(
  }
-------------------
NSSummaryEndpoint.java
      long dirObjectId = getDirObjectId(names);
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/DirectoryEntityHandler.java
  public DUResponse getDuResponse(
  }
-------------------
NSSummaryEndpoint.java
      // DU for key doesn't have subpaths
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/KeyEntityHandler.java
  public DUResponse getDuResponse(
  }
-------------------
NSSummaryEndpoint.java
      duResponse.setStatus(ResponseStatus.PATH_NOT_FOUND);
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/UnknownEntityHandler.java
  public DUResponse getDuResponse(
  }
-------------------
NSSummaryEndpoint.java
      List<OmVolumeArgs> volumes = listVolumes();
      quotaUsageResponse.setQuotaUsed(quotaUsedInBytes);

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/RootEntityHandler.java
  public QuotaUsageResponse getQuotaResponse()
  }
-------------------
NSSummaryEndpoint.java
      List<OmBucketInfo> buckets = listBucketsUnderVolume(names[0]);
      quotaUsageResponse.setQuotaUsed(quotaUsedInBytes);

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/VolumeEntityHandler.java
  public QuotaUsageResponse getQuotaResponse()
  }
-------------------
NSSummaryEndpoint.java
      String bucketKey = omMetadataManager.getBucketKey(names[0], names[1]);
      quotaUsageResponse.setQuotaUsed(quotaUsedInBytes);

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/BucketEntityHandler.java
  public QuotaUsageResponse getQuotaResponse()
  }
-------------------
NSSummaryEndpoint.java
      quotaUsageResponse.setResponseCode(ResponseStatus.PATH_NOT_FOUND);
      quotaUsageResponse.setResponseCode(ResponseStatus.PATH_NOT_FOUND);

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/UnknownEntityHandler.java
  public QuotaUsageResponse getQuotaResponse()
  }
-------------------
NSSummaryEndpoint.java
      quotaUsageResponse.setResponseCode(
          ResponseStatus.TYPE_NOT_APPLICABLE);

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/DirectoryEntityHandler.java
  public QuotaUsageResponse getQuotaResponse()
  }
-------------------
NSSummaryEndpoint.java
      List<OmBucketInfo> allBuckets = listBucketsUnderVolume(null);
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/RootEntityHandler.java
  public FileSizeDistributionResponse getDistResponse()
  }
-------------------
NSSummaryEndpoint.java
      List<OmBucketInfo> buckets = listBucketsUnderVolume(names[0]);
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/VolumeEntityHandler.java
  public FileSizeDistributionResponse getDistResponse()
  }
-------------------
NSSummaryEndpoint.java
      long bucketObjectId = getBucketObjectId(names);
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/BucketEntityHandler.java
  public FileSizeDistributionResponse getDistResponse()
  }
-------------------
NSSummaryEndpoint.java
      long dirObjectId = getDirObjectId(names);
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/DirectoryEntityHandler.java
  public FileSizeDistributionResponse getDistResponse()
  }
-------------------
NSSummaryEndpoint.java
      // key itself doesn't have file size distribution
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/KeyEntityHandler.java
  public FileSizeDistributionResponse getDistResponse()
  }
-------------------
NSSummaryEndpoint.java
      distResponse.setStatus(ResponseStatus.PATH_NOT_FOUND);
      break;

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/UnknownEntityHandler.java
  public FileSizeDistributionResponse getDistResponse()
  }
-------------------
NSSummaryEndpoint.java
   * Return the entity type of client's request, check path existence.
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/EntityHandler.java
   * Return the entity type of client's request, check path existence.
  }
-------------------
NSSummaryEndpoint.java
   * Given a existent path, get the bucket object ID.
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/BucketHandler.java
   * Given a existent path, get the bucket object ID.
  }
-------------------
NSSummaryEndpoint.java
   * Given a valid path request for a directory,
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/FSOBucketHandler.java
   * Given a valid path request for a directory,
  }
-------------------
NSSummaryEndpoint.java
   * Given a valid path request and a cutoff length where should be iterated
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/FSOBucketHandler.java
   * Given a valid path request and a cutoff length where should be iterated
  }
-------------------
NSSummaryEndpoint.java
  static String[] parseRequestPath(String path) {
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/EntityHandler.java
  public static String[] parseRequestPath(String path) {
  }
-------------------
NSSummaryEndpoint.java
   * Example: /vol1/buck1/a/b/c/d/e/file1.txt -> a/b/c/d/e/file1.txt.
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/BucketHandler.java
   * Example: /vol1/buck1/a/b/c/d/e/file1.txt -> a/b/c/d/e/file1.txt.
  }
-------------------
NSSummaryEndpoint.java
   * @param path
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/BucketHandler.java
   * @param path
  }
-------------------
NSSummaryEndpoint.java
  private boolean volumeExists(String volName) throws IOException {
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/EntityHandler.java
  static boolean volumeExists(ReconOMMetadataManager omMetadataManager,
  }
-------------------
NSSummaryEndpoint.java
  private boolean bucketExists(String volName, String bucketName)
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/BucketHandler.java
  boolean bucketExists(String volName, String bucketName)
  }
-------------------
NSSummaryEndpoint.java
   * Given an object ID, return total count of keys under this object.
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/EntityHandler.java
   * Given an object ID, return total count of keys under this object.
  }
-------------------
NSSummaryEndpoint.java
   * Given an object ID, return total count of directories under this object.
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/EntityHandler.java
   * Given an object ID, return total count of directories under this object.
  }
-------------------
NSSummaryEndpoint.java
   * Given an object ID, return total data size (no replication)
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/EntityHandler.java
   * Given an object ID, return total data size (no replication)
  }
-------------------
NSSummaryEndpoint.java
   * Given an object ID, return the file size distribution.
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/EntityHandler.java
   * Given an object ID, return the file size distribution.
  }
-------------------
NSSummaryEndpoint.java
   * Return all volumes in the file system.
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/EntityHandler.java
   * Return all volumes in the file system.
  }
-------------------
NSSummaryEndpoint.java
   * List all buckets under a volume, if volume name is null, return all buckets
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/EntityHandler.java
   * List all buckets under a volume, if volume name is null, return all buckets
  }
-------------------
NSSummaryEndpoint.java
  private long calculateDUForVolume(String volumeName)
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/EntityHandler.java
  long calculateDUForVolume(String volumeName)
  }
-------------------
NSSummaryEndpoint.java
  // FileTable's key is in the format of "parentId/fileName"
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/FSOBucketHandler.java
  // FileTable's key is in the format of "parentId/fileName"
  }
-------------------
NSSummaryEndpoint.java
   * This method handles disk usage of direct keys.
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/FSOBucketHandler.java
   * This method handles disk usage of direct keys.
  }
-------------------
NSSummaryEndpoint.java
  private long getKeySizeWithReplication(OmKeyInfo keyInfo) {
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/BucketHandler.java
  public long getKeySizeWithReplication(OmKeyInfo keyInfo) {
  }
-------------------
NSSummaryEndpoint.java
   * Helper function to check if a path is a directory, key, or invalid.
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/FSOBucketHandler.java
   * Helper function to check if a path is a directory, key, or invalid.
  }
-------------------
NSSummaryEndpoint.java
  private static String normalizePath(String path) {
  }

hadoop-ozone/recon/src/main/java/org/apache/hadoop/ozone/recon/api/handlers/EntityHandler.java
  private static String normalizePath(String path) {
  }
-------------------'''
lines = data.splitlines(True)
# skip hyphens
lines = lines[1:len(lines)]

# create the next replacement dictionary from the data lines
def getNextReplacement():
    global lines
    while len(lines) != 0:
        r = createReplacement(lines[0:7])
        lines = lines[8:len(lines)]
        yield r

def createReplacement(data):
  d = {
      "oldFile": data[0].rstrip(),
      "oldStart": data[1],
      "oldEnd": data[2],
      "newFile": data[4].rstrip(),
      "newStart": data[5],
      "newEnd": data[6]
      }
  return d

inpath = '/home/gbj/incoming/'
handlerpath = '/home/gbj/incoming/build-master/'
fin = open(inpath + 'NSSummaryEndpoint2.java', 'rt', encoding='utf-8')
fout = open(inpath + 'DummyEndpoint.java', 'wt', encoding= 'utf-8')

# skip the lines in the old file
def skipOldLines(fin, data, l):
    while True:
        if l == data['oldEnd']:
            return
        l = fin.readline()
        if l == "":
            error('unexpected error')
            return

#insert the lines from the new file
def insertNewLines(fout, data):
    handlerIn = open(handlerpath + data['newFile'], 'rt', encoding='utf-8')
    while True:
        l = handlerIn.readline()
        if l == "":
            print(data['newStart'])
            error('unexpected error')
            handlerIn.close()
            return
        if l == data['newStart']:
            while True:
                fout.write(l)
                l = handlerIn.readline()
                if l == "":
                    handlerIn.close()
                    error('unexpected error')
                    return
                if l == data['newEnd']:
                    handlerIn.close()
                    fout.write(l)
                    return
                
                
# copy the data from the old file to the new, replacing
#  the appropriate sections as described in each replacement dictionary
for data in getNextReplacement():
    while True:
        l = fin.readline()
        if l == data['oldStart']:
            skipOldLines(fin, data, l)
            insertNewLines(fout, data)
            break
        else:
            fout.write(l)

# once all replacements are done, copy out the rest of the old file
while True:
    l = fin.readline()
    if l == "":
        break
    fout.write(l)
fout.close()    
    

#    pp.pprint(data)





