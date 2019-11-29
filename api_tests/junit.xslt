<?xml version="1.0" encoding="utf-8"?>
<!-- from https://stackoverflow.com/questions/9470060/what-xslt-converts-junit-xml-format-to-junit-plain-format -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="text" indent="no"/>

  <xsl:template match="/testsuite">
    Testsuite: <xsl:value-of select="@name" />
    <xsl:text>
    Tests run: </xsl:text>
    <xsl:value-of select="@tests" />
    <xsl:text>, Failures: </xsl:text>
    <xsl:value-of select="@failures" />
    <xsl:text>, Errors: </xsl:text>
    <xsl:value-of select="@errors" />
    <xsl:text>, Time elapsed: </xsl:text>
    <xsl:value-of select="@time" />
    <xsl:text> sec</xsl:text>
    <xsl:apply-templates select="system-out" />
    <xsl:apply-templates select="system-err" />
    <xsl:text>
    --------- ----------- ---------
    </xsl:text>
    <xsl:apply-templates select="testcase" />
  </xsl:template>

  <xsl:template match="testcase">
    <xsl:text>
    Testcase: </xsl:text>
    <xsl:value-of select="@name" />
    <xsl:text> took </xsl:text>
    <xsl:value-of select="@time" />
  </xsl:template>

  <xsl:template match="system-out">
    <xsl:text>
    ------ Standard output ------
    </xsl:text>
    <xsl:value-of select="." />
  </xsl:template>

  <xsl:template match="system-err">
    <xsl:text>
    ------ Error output ------
    </xsl:text>
    <xsl:value-of select="." />
  </xsl:template>

</xsl:stylesheet>