from chainer import distributions
from chainer import testing
import numpy


@testing.parameterize(*testing.product({
    'shape': [(3, 2), (1,)],
    'is_variable': [True, False],
    'sample_shape': [(3, 2), ()],
}))
@testing.fix_random()
@testing.with_requires('scipy')
class TestBeta(testing.distribution_unittest):

    scipy_onebyone = True

    def setUp_configure(self):
        from scipy import stats
        self.dist = distributions.Beta
        self.scipy_dist = stats.beta

        self.test_targets = set([
            "batch_shape", "entropy", "event_shape", "log_prob", "mean",
            "sample", "support", "variance"])

        a = numpy.random.uniform(0, 10, self.shape).astype(numpy.float32)
        b = numpy.random.uniform(0, 10, self.shape).astype(numpy.float32)
        self.params = {"a": a, "b": b}
        self.scipy_params = {"a": a, "b": b}

        self.support = "[0, 1]"

    def sample_for_test(self):
        smp = numpy.random.uniform(
            size=self.sample_shape + self.shape).astype(numpy.float32)
        return smp


testing.run_module(__name__, __file__)

"""
import unittest

from chainer import distributions
from chainer import testing
import numpy
from scipy import stats


def params_init(shape):
    a = numpy.random.uniform(0, 10, shape).astype(numpy.float32)
    b = numpy.random.uniform(0, 10, shape).astype(numpy.float32)
    params = {"a": a, "b": b}
    sp_params = {"a": a, "b": b}
    return params, sp_params


def sample_for_test(shape):
    smp = numpy.random.uniform(size=shape).astype(numpy.float32)
    return smp


tests = set(["batch_shape", "entropy", "event_shape", "log_prob", "mean",
             "sample", "support", "variance"])


@testing.distribution_unittest(distributions.Beta, stats.beta,
                               params_init, sample_for_test,
                               tests=tests, support="[0, 1]")
class TestBeta(unittest.TestCase):
    pass


testing.run_module(__name__, __file__)
"""
